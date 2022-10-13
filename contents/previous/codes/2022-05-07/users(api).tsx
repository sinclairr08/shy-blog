import { NextApiRequest, NextApiResponse } from "next";
import { PrismaClient } from "@prisma/client";

const client = new PrismaClient();

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method === "GET") {
    const users = await client.users.findMany({
      include: {
        shops: {
          select: {
            name: true,
          },
        },
      },
    });

    res.json({ ok: true, users });
  }

  if (req.method === "POST") {
    const {
      body: {
        data: { name },
      },
    } = req;
    const createUser = await client.users.create({
      data: {
        username: name,
      },
    });

    res.json({ ok: true });
  }

  if (req.method === "PUT") {
    const {
      body: {
        data: { id, name },
      },
    } = req;
    const updateUser = await client.users.update({
      where: {
        id: +id,
      },
      data: {
        username: name,
      },
    });

    res.json({ ok: true });
  }

  if (req.method === "DELETE") {
    const {
      body: { id },
    } = req;

    const deleteUser = await client.users.delete({
      where: {
        id: +id,
      },
    });
  }
}
