import { FieldErrors, useForm } from "react-hook-form";

interface HookFormTypes {
  id: string;
  pw: string;
  age: number;
}

const HookForm = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<HookFormTypes>();

  const onValid = (data: HookFormTypes) => console.log(data);
  const onInValid = (error: FieldErrors) => console.log(error);

  return (
    <form onSubmit={handleSubmit(onValid, onInValid)}>
      <input
        {...register("id", {
          validate: {
            noAdmin: (value) =>
              !value.includes("admin") || "admin is not allowed",
          },
        })}
        type="text"
        placeholder="ID"
      />
      <span>{errors.id?.message}</span>
      <input {...register("pw")} type="password" placeholder="PW" />
      <input {...register("age")} type="number" placeholder="AGE" />
      <input type="submit" />
    </form>
  );
};

export default HookForm;
