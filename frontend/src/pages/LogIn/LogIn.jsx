import { useState } from "react";
import { useNavigate } from "react-router-dom";

import Logo from "../../assets/logo.png";

import "./LogIn.css";

import Button from "../../components/Button/Button.jsx";
import { postLogin } from "../../services/loginApi";

export default function LogIn() {

    const navigate = useNavigate();

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    async function handleLogin(e) {

        e.preventDefault();

        setError("");

        try {

            await postLogin(username, password);

            navigate("/transactions");

        } catch (err) {

            setError(err.message);

        }
    }

    return (
        <div className="LoginBlock">

            <img
                src={Logo}
                className="Logo"
                alt="logo"
                width="60"
                height="60"
            />

            <h1>Log In</h1>

            <h3>
                Турбота про власний бюджет — це турбота про своє майбутнє.
            </h3>

            <form className="LoginForm" onSubmit={handleLogin}>

                <label htmlFor="username">
                    Ім'я користувача
                </label>

                <input
                    type="text"
                    id="username"
                    name="username"
                    autoComplete="nickname"
                    placeholder="Ім'я користувача"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                />

                <label htmlFor="password">
                    Пароль
                </label>

                <input
                    type="password"
                    id="password"
                    placeholder="Пароль"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />

                {error && (
                    <p className="error">
                        {error}
                    </p>
                )}

                <Button type="submit">
                    Увійти
                </Button>

            </form>

            <br />

            <label className="login-link">
                Ще не маєте акаунта?{" "}
                <a href="/signup">
                    Зареєструватися
                </a>
            </label>

        </div>
    );
}