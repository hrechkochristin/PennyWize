const API_URL = "http://127.0.0.1:8000";

export async function getTransactions() {
    const token = localStorage.getItem("access_token");
    const response = await fetch(
        `${API_URL}/transactions/?sort_by=date&order=desc&range_by=amount`,
        {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        }
    );
    if (!response.ok) {
        throw new Error("Не вдалося отримати транзакції");
    }
    return await response.json();
}


export async function postTransaction(transaction) {
    const token = localStorage.getItem("access_token");

    const response = await fetch(`${API_URL}/transactions/`, {
        method: "POST",

        headers: {
            "Content-Type": "application/json",

            Authorization: `Bearer ${token}`,
        },

        body: JSON.stringify(transaction),
    });

    if (!response.ok) {
        let message = "Не вдалося створити транзакцію.";

        try {
            const errorData = await response.json();

            if (typeof errorData.detail === "string") {
                message = errorData.detail;
            }
        } catch {
            // Backend не повернув JSON
        }

        throw new Error(message);
    }

    return await response.json();
}


export async function getCategories() {
    const token = localStorage.getItem("access_token");

    const response = await fetch(`${API_URL}/categories/`, {
        method: "GET",

        headers: {
            Authorization: `Bearer ${token}`,
        },
    });

    if (!response.ok) {
        throw new Error("Не вдалося завантажити категорії.");
    }

    return await response.json();
}
