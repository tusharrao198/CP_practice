function maxCost(cost, labels, dailyCount)
{
    let max_ = 0
    let legals = 0
    let c = [];
    for (i = 0; i < labels.length; i++)
    {
        if (legals === dailyCount){
            c.push(max_);
            legals = 0;
            max_ = 0;
        }
        if (labels[i] === "legal")
        {
            legals = legals + 1;
            max_ = max_ + cost[i];
        }
        if (labels[i] == "illegal")
        {
            max_ = max_ + cost[i];
        }
    } 
    return Math.max(...c);
}

console.log(maxCost( [2,5,3,11,1],["legal", "illegal","legal", "illegal","legal"], 2))