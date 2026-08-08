import "./TransactionGroup.css";

import TransactionCard from "../TransactionCard/TransactionCard.jsx";

import {
    formatDate,
    formatAmount,
    calculateDailyStats
} from "../../../pages/Transactions/helpers";


export default function TransactionGroup({
    date,
    transactions
}) {
    const stats = calculateDailyStats(transactions);

    return (
        <section className="TransactionGroup">

            <div className="TransactionGroupHeader">

                <h2 className="TransactionDate">
                    {formatDate(date)}
                </h2>

                <div className="TransactionStats">

                    {Object.entries(stats).map(
                        ([currency, stat]) => (
                            <div
                                className="TransactionStat"
                                key={currency}
                            >

                                <span className="StatIncome">
                                    +{formatAmount(
                                        stat.income,
                                        currency
                                    )}
                                </span>

                                <span className="StatExpense">
                                    -{formatAmount(
                                        stat.expense,
                                        currency
                                    )}
                                </span>

                                <span
                                    className={
                                        stat.balance >= 0
                                            ? "StatBalance positive"
                                            : "StatBalance negative"
                                    }
                                >
                                    {stat.balance >= 0
                                        ? "+"
                                        : "-"
                                    }

                                    {formatAmount(
                                        Math.abs(stat.balance),
                                        currency
                                    )}
                                </span>

                            </div>
                        )
                    )}

                </div>

            </div>


            <div className="TransactionGroupCards">

                {transactions.map((transaction) => (

                    <TransactionCard
                        key={transaction.id}
                        transaction={transaction}
                        formattedAmount={formatAmount(
                            transaction.amount,
                            transaction.currency
                        )}
                    />

                ))}

            </div>

        </section>
    );
}