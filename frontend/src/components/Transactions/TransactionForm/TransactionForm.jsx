import { useEffect, useState } from "react";

import {
    getCategories,
    postTransaction,
} from "../../../services/transactionApi";

import "./TransactionForm.css";


export default function TransactionForm({ onCreated }) {

    const [categories, setCategories] = useState([]);

    const [name, setName] = useState("");
    const [description, setDescription] = useState("");
    const [amount, setAmount] = useState("");
    const [type, setType] = useState("expense");
    const [currency, setCurrency] = useState("UAH");
    const [accountName, setAccountName] = useState("");
    const [date, setDate] = useState(
        new Date().toISOString().slice(0, 16)
    );
    const [categoryId, setCategoryId] = useState("");

    const [loading, setLoading] = useState(false);
    const [categoriesLoading, setCategoriesLoading] = useState(true);
    const [error, setError] = useState("");


    useEffect(() => {
        async function loadCategories() {
            try {
                const data = await getCategories();

                setCategories(data);

                if (data.length > 0) {
                    setCategoryId(String(data[0].id));
                }

            } catch (err) {
                setError(err.message);
            } finally {
                setCategoriesLoading(false);
            }
        }

        loadCategories();
    }, []);


    const selectedCategory = categories.find(
        category => String(category.id) === String(categoryId)
    );


    async function handleSubmit(event) {
        event.preventDefault();

        setError("");

        if (!name.trim()) {
            setError("Введіть назву транзакції.");
            return;
        }

        if (!amount || Number(amount) <= 0) {
            setError("Введіть коректну суму.");
            return;
        }

        if (!categoryId) {
            setError("Оберіть категорію.");
            return;
        }


        const transaction = {
            name: name.trim(),

            description: description.trim() || null,

            amount: Number(amount),

            type,

            currency,

            account_name: accountName.trim() || null,

            date: new Date(date).toISOString(),

            category_id: Number(categoryId),
        };


        try {
            setLoading(true);

            const createdTransaction =
                await postTransaction(transaction);


            // Очищаємо форму
            setName("");
            setDescription("");
            setAmount("");
            setAccountName("");

            setDate(
                new Date().toISOString().slice(0, 16)
            );


            // Передаємо створену транзакцію батьківському компоненту
            if (onCreated) {
                onCreated(createdTransaction);
            }

        } catch (err) {
            setError(err.message);

        } finally {
            setLoading(false);
        }
    }


    return (
        <form
            className="TransactionForm"
            onSubmit={handleSubmit}
            style={{
                "--category-color":
                    selectedCategory?.color || "#CBE7C2",
            }}
        >

            <div className="TransactionFormHeader">

                <div
                    className="TransactionFormIcon"
                    style={{
                        backgroundColor:
                            selectedCategory?.color ||
                            "#CBE7C2",
                    }}
                >
                    {selectedCategory?.icon || "💰"}
                </div>

                <div>
                    <h2>Нова транзакція</h2>

                    <p>
                        Додайте нову операцію до бюджету
                    </p>
                </div>

            </div>


            {error && (
                <p className="TransactionFormError">
                    {error}
                </p>
            )}


            <div className="TransactionFormField">

                <label htmlFor="transaction-name">
                    Назва
                </label>

                <input
                    id="transaction-name"
                    type="text"
                    placeholder="Наприклад, Кава"
                    value={name}
                    onChange={(event) =>
                        setName(event.target.value)
                    }
                    required
                />

            </div>


            <div className="TransactionFormField">

                <label htmlFor="transaction-description">
                    Опис
                </label>

                <textarea
                    id="transaction-description"
                    placeholder="Додатковий опис"
                    value={description}
                    onChange={(event) =>
                        setDescription(event.target.value)
                    }
                    rows="3"
                />

            </div>


            <div className="TransactionFormRow">

                <div className="TransactionFormField">

                    <label htmlFor="transaction-amount">
                        Сума
                    </label>

                    <input
                        id="transaction-amount"
                        type="number"
                        min="0"
                        step="0.01"
                        placeholder="0.00"
                        value={amount}
                        onChange={(event) =>
                            setAmount(event.target.value)
                        }
                        required
                    />

                </div>


                <div className="TransactionFormField">

                    <label htmlFor="transaction-currency">
                        Валюта
                    </label>

                    <select
                        id="transaction-currency"
                        value={currency}
                        onChange={(event) =>
                            setCurrency(event.target.value)
                        }
                    >
                        <option value="UAH">UAH</option>
                        <option value="USD">USD</option>
                        <option value="EUR">EUR</option>
                        <option value="GBP">GBP</option>
                    </select>

                </div>

            </div>


            <div className="TransactionFormField">

                <label>Тип</label>

                <div className="TransactionType">

                    <button
                        type="button"
                        className={
                            type === "expense"
                                ? "TransactionTypeButton active expense"
                                : "TransactionTypeButton"
                        }
                        onClick={() =>
                            setType("expense")
                        }
                    >
                        − Витрата
                    </button>

                    <button
                        type="button"
                        className={
                            type === "income"
                                ? "TransactionTypeButton active income"
                                : "TransactionTypeButton"
                        }
                        onClick={() =>
                            setType("income")
                        }
                    >
                        + Дохід
                    </button>

                </div>

            </div>


            <div className="TransactionFormField">

                <label htmlFor="transaction-category">
                    Категорія
                </label>

                {categoriesLoading ? (

                    <p className="TransactionFormLoading">
                        Завантаження категорій...
                    </p>

                ) : (

                    <select
                        id="transaction-category"
                        value={categoryId}
                        onChange={(event) =>
                            setCategoryId(event.target.value)
                        }
                        required
                    >

                        {categories.map(category => (

                            <option
                                key={category.id}
                                value={category.id}
                            >
                                {category.icon} {category.name}
                            </option>

                        ))}

                    </select>

                )}

            </div>


            <div className="TransactionFormField">

                <label htmlFor="transaction-account">
                    Рахунок
                </label>

                <input
                    id="transaction-account"
                    type="text"
                    placeholder="Наприклад, Monobank"
                    value={accountName}
                    onChange={(event) =>
                        setAccountName(event.target.value)
                    }
                />

            </div>


            <div className="TransactionFormField">

                <label htmlFor="transaction-date">
                    Дата
                </label>

                <input
                    id="transaction-date"
                    type="datetime-local"
                    value={date}
                    onChange={(event) =>
                        setDate(event.target.value)
                    }
                    required
                />

            </div>


            <button
                type="submit"
                className="TransactionSubmit"
                disabled={loading || categoriesLoading}
            >
                {loading
                    ? "Збереження..."
                    : "Додати транзакцію"
                }
            </button>

        </form>
    );
}
