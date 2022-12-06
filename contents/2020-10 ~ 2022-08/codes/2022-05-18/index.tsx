import useSWR from "swr";
import axios from "axios";
import { useEffect } from "react";

interface ShopsReturn {
  ok: boolean;
  shops: string[];
}

export default function Test() {
  /*
  const [shopList, setShopList] = useState<string[]>([]);

  useEffect(() => {
    axios.get("/api/shops").then((res) => setShopList(res.data.shops));
  }, []);
   */

  const { data, error } = useSWR<ShopsReturn>("/api/shops");

  return <h1>{data.ok}</h1>;
}
