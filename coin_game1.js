function optimalStrategyOfGame(arr, n)
{
 
    let memo = {};
 
    // recursive top down memoized solution
    function solve(i, j)
    {
        if ( (i > j) || (i >= n) || (j < 0))
            return 0;
 
        let k = (i, j);
        if (memo.hasOwnProperty(k))
            return memo[k];
 
        // if the user chooses ith coin, the opponent can choose from i+1th or jth coin.
        // if he chooses i+1th coin, user is left with [i+2,j] range.
        // if opp chooses jth coin, then user is left with [i+1,j-1] range to choose from.
        // Also opponent tries to choose
        // in such a way that the user has minimum value left.
        let option1 = arr[i] + Math.min(solve(i+2, j), solve(i+1, j-1));
 
        // if user chooses jth coin, opponent can choose ith coin or j-1th coin.
        // if opp chooses ith coin,user can choose in range [i+1,j-1].
        // if opp chooses j-1th coin, user can choose in range [i,j-2].
        let option2 = arr[j] + Math.min(solve(i+1, j-1), solve(i, j-2));
 
        // since the user wants to get maximum money
        memo[k] = Math.max(option1, option2);
        return memo[k];
    }
 
    return solve(0, n-1);
}
 
 
// Driver code
let arr1 = [ 8, 15, 3, 7 ];
let n = arr1.length;
console.log(optimalStrategyOfGame(arr1, n));
 
let arr2 = [ 2, 2, 2, 2 ];
n = arr2.length;
console.log(optimalStrategyOfGame(arr2, n));
 
 
let arr3 = [ 20, 30, 2, 2, 2, 10 ];
n = arr3.length;
console.log(optimalStrategyOfGame(arr3, n));
 
 
 