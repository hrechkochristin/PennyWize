import "./Button.css";

export default function Button({
    children,
    onClick,
    isActive,
    type = "button",
}) {
    return (
        <button
            className={`button ${isActive ? "active" : ""}`}
            onClick={onClick}
            type={type}
        >
            {children}
        </button>
    );
}