class ArtGallery{
    constructor(creator) {
        this.creator = creator
        this.possibleArticles = { "picture":200,"photo":50,"item":250 }
        this.listOfArticles = [];
        this.guests = [];
    }
    addArticle(articleModel, articleName, quantity ){
        articleModel = articleModel.toLowerCase();
        if (this.possibleArticles[articleModel]=== undefined){
            throw Error("This article model is not included in this gallery!")
        }
        let findArticle = this.listOfArticles.filter((el)=> el.articleName === articleName && el.articleModel === articleModel)


            if (findArticle.length > 0){
               findArticle[0].quantity += quantity;


            }else {


            this.listOfArticles.push({articleModel, articleName, quantity})}
        return `Successfully added article ${articleName} with a new quantity- ${quantity}.`

    }
    inviteGuest(guestName, personality){
        const point = {'Vip': 500,'Middle':250};
        let findGuest = this.guests.filter((el)=> el.guestName === guestName)
        let points = 50;
        if (findGuest.length > 0) {
            throw Error(`${guestName} has already been invited.`);
        }
        if (!personality){
            points = 50;
        }else {
            points = point[personality];
        }

        this.guests.push({guestName,points,purchaseArticle:0})
        return `You have successfully invited ${guestName}!`
    }
    buyArticle(articleModel, articleName, guestName){
       let findArticle = this.listOfArticles.filter((el)=> el.articleName === articleName)
       let findGuest = this.guests.filter((el)=> el.guestName === guestName)
        if (findArticle.length <= 0 || findArticle[0].articleModel !== articleModel){
            throw Error("This article is not found.")
        }
        if(findArticle[0].quantity === 0){
            return `The ${findArticle[0].articleName} is not available.`
        }
        if (findGuest.length <= 0){
            return "This guest is not invited."
        }
        if(findGuest[0].points >=this.possibleArticles[articleModel]){
            findGuest[0].points -= this.possibleArticles[articleModel];
            findGuest[0].purchaseArticle += 1;
            findArticle[0].quantity -= 1;
            return `${guestName} successfully purchased the article worth ${this.possibleArticles[articleModel]} points.`
        }else {
            return "You need to more points to purchase the article."
        }
    }
    showGalleryInfo(criteria){
        let result = [];
        if(criteria ==='article'){
            result.push("Articles information:")
            for (const element of this.listOfArticles) {
                result.push(`${element.articleModel} - ${element.articleName} - ${element.quantity}`);
            }
        }else if(criteria === 'guest'){
            result.push("Guests information:")
            for (const element of this.guests) {
                result.push(`${element.guestName} - ${element.purchaseArticle}`);
            }
        }
        return result.join('\n');
    }

}



const artGallery = new ArtGallery('Curtis Mayfield');
artGallery.addArticle('picture', 'Mona Liza', 3);
artGallery.addArticle('Item', 'Ancient vase', 2);
artGallery.addArticle('picture', 'Mona Liza', 1);
artGallery.inviteGuest('John', 'Vip');
artGallery.inviteGuest('Peter', 'Middle');
artGallery.buyArticle('picture', 'Mona Liza', 'John');
artGallery.buyArticle('item', 'Ancient vase', 'Peter');
console.log(artGallery.showGalleryInfo('article'));
console.log(artGallery.showGalleryInfo('guest'));