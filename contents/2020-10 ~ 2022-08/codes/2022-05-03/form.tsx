import React, { useState } from "react";

const Form = () => {
  const [name, setName] = useState("");
  const onNameChange = (event: React.SyntheticEvent<HTMLInputElement>) => {
    const {
      currentTarget: { value },
    } = event;
    setName(value);
  };

  const onSubmit = (event: React.SyntheticEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log(name);
  };
  return (
    <form onSubmit={onSubmit}>
      <input
        type="text"
        onChange={onNameChange}
        value={name}
        placeholder="name"
      />
      <input type="submit" />
    </form>
  );
};

export default Form;
