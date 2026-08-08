import TransactionsLogo from "../../assets/transactions_logo.png";
import "./Transactions.css";

import Header from "../../components/Header/Header.jsx";
import TransactionGroup from "../../components/Transactions/TransactionGroup/TransactionGroup.jsx";
import TransactionForm from "../../components/Transactions/TransactionForm/TransactionForm.jsx";

import { useEffect, useState } from "react";
import { getTransactions } from "../../services/transactionApi";

import {
    groupTransactionsByDate,
    formatDate,
    formatAmount
} from "./helpers";


export default function Transactions() {
    const [showForm, setShowForm] = useState(false);

    const [transactions, setTransactions] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");


    useEffect(() => {
        async function loadTransactions() {
            try {
                const data = await getTransactions();
                setTransactions(data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        }

        loadTransactions();
    }, []);


    if (loading) {
        return (
            <div className="TransactionsPage">
                <p>Завантаження...</p>
            </div>
        );
    }


    if (error) {
        return (
            <div className="TransactionsPage">
                <p className="Error">{error}</p>
            </div>
        );
    }


    const groupedTransactions =
        groupTransactionsByDate(transactions);


    return (
        <div className="TransactionsPage">

            <Header />

            <section className="TransactionsHero">

                <img
                    src={TransactionsLogo}
                    alt="Transactions"
                    className="TransactionsLogo"
                />

                <div>
                    <h1>Transactions</h1>

                    <p>
                        Турбота про власний бюджет — це турбота
                        про своє майбутнє.
                    </p>
                </div>

                <button
                    className="AddTransactionButton"
                    onClick={() => setShowForm(true)}
                >
                    + Додати транзакцію
                </button>

            </section>


            {showForm && (
                <div
                    className="TransactionModalOverlay"
                    onClick={() => setShowForm(false)}
                >

                    <div
                        className="TransactionModal"
                        onClick={(event) => event.stopPropagation()}
                    >

                        <button
                            className="TransactionModalClose"
                            onClick={() => setShowForm(false)}
                            aria-label="Закрити"
                        >
                            ×
                        </button>

                        <TransactionForm
                            onCreated={(transaction) => {

                                setTransactions(prev => [
                                    transaction,
                                    ...prev
                                ]);

                                setShowForm(false);
                            }}
                        />

                    </div>

                </div>
            )}

            <section className="TransactionList">

                {Object.entries(groupedTransactions).map(
                    ([date, transactions]) => (

                        <TransactionGroup
                            key={date}
                            date={date}
                            transactions={transactions}
                        />

                    )
                )}

            </section>

        </div>
    );
}