function solution(command) {
    let commands = {
        upvote: () => {
            this.upvotes++
        },
        downvote: () => {
            this.downvotes++
        },
        score: () => {
            let totalScore = this.upvotes - this.downvotes;
            let totalVote = this.upvotes + this.downvotes;
            let obfuscated = Math.ceil(Math.max(this.upvotes, this.downvotes) * 0.25);
            let obfuscatedUpVote = totalVote > 50 ? this.upvotes + obfuscated : this.upvotes;
            let obfuscatedDownVote = totalVote > 50 ? this.downvotes + obfuscated : this.downvotes;

            let rating = 'new';
            if (totalVote < 10) {
                rating = 'new';
            } else if (this.upvotes / totalVote > 0.66) {
                rating = 'hot';
            } else if (this.downvotes <= this.upvotes && totalVote > 100) {
                rating = 'controversial';
            } else if(this.downvotes > this.upvotes) {
                rating = 'unpopular';
            }
            return [obfuscatedUpVote, obfuscatedDownVote, totalScore, rating];

        }
    }
    return commands[command]();
}


let post = {
    id: '3',
    author: 'emil',
    content: 'wazaaaaa',
    upvotes: 100,
    downvotes: 100
};
solution.call(post, 'upvote');
solution.call(post, 'downvote');
let score = solution.call(post, 'score'); // [127, 127, 0, 'controversial']
console.log(score)
solution.call(post, 'downvote');         // (executed 50 times)
score = solution.call(post, 'score');
console.log(score)
// [139, 189, -50, 'unpopular']
