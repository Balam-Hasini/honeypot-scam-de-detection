exports.handler = async (event) => {
  return {
    statusCode: 200,
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      status: "interaction_logged",
      message: "Suspicious request captured",
      ip: event.headers["x-forwarded-for"] || "unknown",
      userAgent: event.headers["user-agent"] || "unknown"
    })
  };
};
