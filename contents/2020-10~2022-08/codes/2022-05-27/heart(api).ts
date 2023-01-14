import { PrismaClient } from "@prisma/client";
import { NextApiRequest, NextApiResponse } from "next";

const client = new PrismaClient();

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const userId = 1;
  const shopId = 1;

  if (req.method === "GET") {
    const shop = await client.shop.findUnique({
      where: {
        id: shopId,
      },
      select: {
        _count: {
          select: {
            hearts: true,
          },
        },
      },
    });
    const isLiked = Boolean(
      await client.heart.findFirst({
        where: {
          createdUserId: userId,
          likedShopId: shopId,
        },
      })
    );

    res.json({ ok: true, isLiked, likes: shop?._count.hearts });
  }

  if (req.method === "POST") {
    const foundHeart = await client.heart.findFirst({
      where: {
        likedShopId: shopId,
        createdUserId: userId,
      },
    });

    if (foundHeart) {
      await client.heart.delete({
        where: {
          id: foundHeart.id,
        },
      });
    } else {
      await client.heart.create({
        data: {
          createdUser: {
            connect: {
              id: userId,
            },
          },
          likedShop: {
            connect: {
              id: shopId,
            },
          },
        },
      });
    }
  }

  res.json({ ok: true });
}
