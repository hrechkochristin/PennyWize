const API_URL = "http://127.0.0.1:8000";

export async function postLogin(username, password) {
    const formData = new URLSearchParams();
    formData.append("username", username);
    formData.append("password", password);
    const response = await fetch(`${API_URL}/users/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: formData,
    });

    if (!response.ok) {
        throw new Error("Не вдалося увійти.");
    }

    const data = await response.json();
    // Зберігаємо JWT
    localStorage.setItem("access_token", data.access_token);
    return data;
}