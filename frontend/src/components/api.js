export const prorateAllocation = async (data) => {
    const response = await fetch("http://localhost:8000/prorate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
    });
    return response.json();
};
