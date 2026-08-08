import "./TransactionCard.css";


export default function TransactionCard({
    transaction,
    formattedAmount
}) {

    const categoryColor =
        transaction.category?.color || "#E5E5E5";


    return (
        <article
            className="TransactionCard"
            style={{
                "--category-color": categoryColor
            }}
        >

            <div className="TransactionCardIcon">
                {transaction.category?.icon}
            </div>


            <div className="TransactionInfo">

                <h3>
                    {transaction.name}
                </h3>

                {transaction.description && (
                    <p>
                        {transaction.description}
                    </p>
                )}

            </div>


            <span
                className={
                    transaction.type === "income"
                        ? "Income"
                        : "Expense"
                }
            >
                {transaction.type === "income" ? "+" : "-"}
                {formattedAmount}
            </span>

        </article>
    );
}