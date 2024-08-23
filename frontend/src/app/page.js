"use client";

import { useState, useEffect } from "react";

export default function Home() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("/api/hello")
      .then((response) => response.json())
      .then((data) => setMessage(data.message))
      .catch((error) => console.error("Error:", error));
  }, []);

  return (
    <main>
      <h1>Next.js with Django Backend</h1>
      <p>{message}</p>
    </main>
  );
}
