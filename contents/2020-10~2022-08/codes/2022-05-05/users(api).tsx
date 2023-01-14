import { NextApiRequest, NextApiResponse } from "next";
import { PrismaClient } from "@prisma/client";

const client = new PrismaClient();

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method === "GET") {
    const allUsers = await client.users.findMany({
      where: {
        username: "Demian",
      },
    });
    const firstUsers = await client.users.findFirst({
      where: {
        username: "Demian",
      },
    });
    const uniqUsers = await client.users.findUnique({
      where: {
        id: 1,
      },
    });
    const usersWshops = await client.users.findMany({
      include: {
        shops: true,
      },
    });

    const usersWshopsName = await client.users.findMany({
      include: {
        shops: {
          select: {
            name: true,
          },
        },
      },
    });
    res.json({ ok: true });
  }

  if (req.method === "POST") {
    const newUser = await client.users.create({
      data: {
        username: "Frau Eva",
      },
    });
    const newUsers = await client.users.createMany({
      data: [{ username: "Emil Sinclair" }, { username: "Abraxas" }],
    });
    const newUserWshop = await client.users.create({
      data: {
        username: "Frau Eva",
        shops: {
          create: {
            name: "Bella",
            location: "Hanyang",
          },
        },
      },
    });

    const newShopWCreate = await client.shops.create({
      data: {
        name: "IU",
        users: {
          create: {
            username: "jieun",
          },
        },
      },
    });

    const newShopWConnect = await client.shops.create({
      data: {
        name: "IU",
        users: {
          connect: {
            id: 1,
          },
        },
      },
    });

    const newShopWCrOrCon = await client.shops.create({
      data: {
        name: "IU",
        users: {
          connectOrCreate: {
            where: {
              id: 1,
            },
            create: {
              username: "jieun",
            },
          },
        },
      },
    });

    res.json({ ok: true });
  }

  if (req.method === "PUT") {
    const updateUser = await client.users.update({
      where: {
        id: 1,
      },
      data: {
        username: "Franz",
      },
    });
    const updateUsers = await client.users.updateMany({
      where: {
        username: {
          contains: "demian",
        },
        id: {
          lte: 3,
        },
      },
      data: {
        username: "Alfons",
      },
    });

    res.json({ ok: true });
  }

  if (req.method === "DELETE") {
    const deleteUser = await client.users.delete({
      where: {
        id: 3,
      },
    });
    const deleteUsers = await client.users.deleteMany({
      where: {
        username: {
          contains: "Alfons",
        },
      },
    });
  }
}
