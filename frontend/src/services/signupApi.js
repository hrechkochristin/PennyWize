const API_URL = "http://127.0.0.1:8000";

export async function postSignup(username, email, password) {
    const response = await fetch(`${API_URL}/users/signup`, {
        method: "POST",

        headers: {
            "Content-Type": "application/json",
        },

        body: JSON.stringify({
            username,
            email,
            password,
        }),
    });

    if (!response.ok) {
        let message = "Не вдалося зареєструватися.";

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

    const data = await response.json();

    localStorage.setItem(
        "access_token",
        data.access_token
    );

    return data;
}