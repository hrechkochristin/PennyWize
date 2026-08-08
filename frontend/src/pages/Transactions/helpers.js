export function groupTransactionsByDate(transactions) {
    return transactions.reduce((groups, transaction) => {
        const date = transaction.date.split("T")[0];
        if (!groups[date]) {
            groups[date] = [];
        }
        groups[date].push(transaction);
        return groups;
    }, {});
}

export function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString("uk-UA", {
        day: "numeric",
        month: "long",
    });
}

const currencySymbols = {
    UAH: "₴",
    USD: "$",
    EUR: "€",
    GBP: "£",
    PLN: "zł",
    CZK: "Kč",
    CHF: "CHF",
    JPY: "¥",
    CNY: "¥",
};

export function formatAmount(amount, currency) {
    const symbol = currencySymbols[currency] || currency;

    const formattedAmount = new Intl.NumberFormat("uk-UA", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
    }).format(Math.abs(amount));

    return `${formattedAmount} ${symbol}`;
}


export function calculateDailyStats(transactions) {
    const stats = {};

    transactions.forEach((transaction) => {
        const currency = transaction.currency;

        if (!stats[currency]) {
            stats[currency] = {
                income: 0,
                expense: 0,
            };
        }

        if (transaction.type === "income") {
            stats[currency].income += Number(transaction.amount);
        } else {
            stats[currency].expense += Number(transaction.amount);
        }
    });

    Object.values(stats).forEach((stat) => {
        stat.balance = stat.income - stat.expense;
    });

    return stats;
}