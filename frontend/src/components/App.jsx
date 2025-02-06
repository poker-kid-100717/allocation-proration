import React, { useState } from "react";
import { prorateAllocation } from "./api";

function App() {
    const [allocation, setAllocation] = useState(100);
    const [investors, setInvestors] = useState([
        { name: "Investor A", requested_amount: 100, average_amount: 100 },
        { name: "Investor B", requested_amount: 25, average_amount: 25 },
    ]);
    const [results, setResults] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = { allocation_amount: allocation, investor_amounts: investors };
        const result = await prorateAllocation(data);
        setResults(result);
    };

    return (
        <div>
            <h1>Allocation Proration Tool</h1>
            <form onSubmit={handleSubmit}>
                <label>Allocation Amount:</label>
                <input type="number" value={allocation} onChange={(e) => setAllocation(e.target.value)} />
                <button type="submit">Prorate</button>
            </form>

            {results && (
                <div>
                    <h2>Results</h2>
                    <ul>
                        {Object.entries(results).map(([name, amount]) => (
                            <li key={name}>{name}: ${amount.toFixed(2)}</li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
}

export default App;