import axios from "axios";
import { useState } from "react";
import { useForm } from "react-hook-form";

interface ImageForm {
  image: FileList;
}

export default function () {
  const { register, handleSubmit } = useForm<ImageForm>();
  const [id, setId] = useState("");
  const onValid = async ({ image }: ImageForm) => {
    if (image && image.length > 0) {
      const {
        data: { uploadURL },
      } = await axios.get("/api/image");

      const formData = new FormData();
      formData.append("file", image[0], "test");
      const { data } = await axios.post(uploadURL, formData);
      setId(data.result.id);
    }
  };
  return (
    <>
      <form onSubmit={handleSubmit(onValid)}>
        <input {...register("image")} type="file" accept="image/*" />
        <button>Submit</button>
      </form>
      {id ? (
        <img src={`https://imagedelivery.net/<your_id>/${id}/public`} />
      ) : (
        <div></div>
      )}
    </>
  );
}
