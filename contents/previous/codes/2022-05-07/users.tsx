import axios from "axios";

export default function Users() {
  const onPostClick = async () => {
    await axios.post("/api/users", {
      headers: { "Content-Type": "application/json" },
      data: {
        name: "Max Demian",
      },
    });
  };
  const onGetClick = async () => {
    const { data } = await axios.get("/api/users");
    console.log(data);
  };
  const onPutClick = async () => {
    await axios.put("/api/users", {
      data: {
        id: 2,
        name: "Max Emila",
      },
    });
  };
  const onDeleteClick = async () => {
    await axios.delete("/api/users", {
      data: {
        id: 2,
      },
    });
  };
  return (
    <div className="flex flex-col space-y-8">
      <button onClick={onPostClick}>POST</button>
      <button onClick={onGetClick}>GET</button>
      <button onClick={onPutClick}>PUT</button>
      <button onClick={onDeleteClick}>DELETE</button>
    </div>
  );
}
