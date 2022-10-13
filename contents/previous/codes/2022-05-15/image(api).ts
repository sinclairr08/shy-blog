import axios from "axios";
import { NextApiRequest, NextApiResponse } from "next";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method === "GET") {
    const imageResponse = await axios(
      `https://api.cloudflare.com/client/v4/accounts/${process.env.CF_ID}/images/v2/direct_upload`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${process.env.CF_API_TOKEN}`,
        },
      }
    );

    const {
      data: {
        result: { uploadURL },
      },
    } = imageResponse;

    res.json({ ok: true, uploadURL });
  }
}
