import { useState } from "react";
import Logo from "../../assets/logo.png";
import Eye from "../../assets/eye.png";
import Eye_hide from "../../assets/eye_hide.png";

import "./SignUp.css";
import Button from "../../components/Button/Button.jsx";

import { useNavigate } from "react-router-dom";
import { postSignup } from "../../services/signupApi.js";

export default function SignUp() {
    const navigate = useNavigate();

    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const [showPassword, setShowPassword] = useState(false);

    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    async function handleSubmit(event) {
        event.preventDefault();

        setError("");

        if (!username || !email || !password) {
            setError("Заповніть усі поля.");
            return;
        }

        try {
            setLoading(true);

            await postSignup(
                username,
                email,
                password
            );

            navigate("/transactions");

        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
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

            <h1>Sign Up</h1>

            <h3>
                Найкращий момент почати контролювати свої фінанси —
                сьогодні.
            </h3>

            <form
                className="LoginForm"
                onSubmit={handleSubmit}
            >

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
                    onChange={(event) =>
                        setUsername(event.target.value)
                    }
                />


                <label htmlFor="email">
                    Електронна пошта
                </label>

                <input
                    type="email"
                    id="email"
                    name="email"
                    autoComplete="email"
                    placeholder="Електронна пошта"
                    value={email}
                    onChange={(event) =>
                        setEmail(event.target.value)
                    }
                />


                <label htmlFor="password">
                    Пароль
                </label>

                <div className="PasswordInputWrapper">

                    <input
                        type={showPassword ? "text" : "password"}
                        id="password"
                        name="password"
                        autoComplete="new-password"
                        placeholder="Пароль"
                        value={password}
                        onChange={(event) =>
                            setPassword(event.target.value)
                        }
                    />

                    <button
                        type="button"
                        className="PasswordToggle"
                        onClick={() =>
                            setShowPassword(!showPassword)
                        }
                        aria-label={
                            showPassword
                                ? "Приховати пароль"
                                : "Показати пароль"
                        }
                    >
                        {showPassword ?
                            <img src={Eye_hide} className="Eye_hide" alt="eye_hide" width="20" height="20"/>
                            : <img src={Eye} className="Eye" alt="eye" width="20" height="20"/>}
                    </button>

                </div>


                {error && (
                    <p className="FormError">
                        {error}
                    </p>
                )}


                <div className="Agreement">

                    <input
                        type="checkbox"
                        id="agreement"
                    />

                    <label htmlFor="agreement">
                        Реєструючись, ви погоджуєтеся з нашими{" "}
                        <a
                            href="/terms"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            Умовами використання
                        </a>{" "}
                        та{" "}
                        <a
                            href="/privacy"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            Політикою конфіденційності
                        </a>.
                    </label>

                </div>


                <Button
                    type="submit"
                    disabled={loading}
                >
                    {loading
                        ? "Реєстрація..."
                        : "Зареєструватися"
                    }
                </Button>

            </form>


            <label htmlFor="login">
                Вже маєте акаунт?{" "}
                <a href="/login">
                    Увійти
                </a>
            </label>

        </div>
    );
}
