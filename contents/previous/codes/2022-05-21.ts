import { NextApiRequest, NextApiResponse } from "next";
import { withIronSessionApiRoute } from "iron-session/next";
import { IronSessionOptions } from "iron-session";
import { PrismaClient } from "@prisma/client";

const client = new PrismaClient();

const findUser = async (id: number) => {
  const foundUser = await client.user.findUnique({
    where: {
      id,
    },
  });
  return foundUser;
};

declare module "iron-session" {
  interface IronSessionData {
    user?: {
      id: number;
    };
  }
}

const options: IronSessionOptions = {
  cookieName: "reservation-site",
  password: "VERYYLONGPASSWORDS1ab1323898esda345q6781!",
};

async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === "GET") {
    const id = req.session.user ? req.session.user.id : 1;
    const foundUser = await findUser(id);

    res.json({ ok: true, foundUser });
  }
  if (req.method === "POST") {
    const {
      body: { userId },
    } = req;

    // Assign value
    req.session.user = {
      id: +userId,
    };

    // Save at a session
    await req.session.save();

    res.json({ ok: true });
  }
}

export default withIronSessionApiRoute(handler, options);
