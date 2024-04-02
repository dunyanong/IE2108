// INDEX.JS

//Get product from handle
request.get(apiURI + '/products/' + target, async function(error, response, body){
    //This requires an error handler
    //Get product from handle.
// Note that this is JS SDK and does not have tags
//This requires an error handler

    //Get product details
    let product;
    try{
    //Check if there is response data
    if(Object.keys(JSON.parse(body)).length>0){
        product = JSON.parse(body);
    }else{
        return render404(req,res,langpack)
    }
    //console.log(product)
    }catch(e){
    return render404(req,res,langpack)
    }
    // console.log(product)

    //Added by Ameera on 9th May 2022: Sort variants from lower to higher price
    product.variants.sort(function(a,b){
    return (a.price - b.price);
    })

    //Catch if no such product or route
    try{
    if(Object.keys(product).length == 0){
        console.log("Error here at index.js - empty product")
        return render404(req,res,langpack)
    }
    }catch(e){
    console.log('Error here if no products')
    return render404(req,res,langpack)
    }

    //Define links
    let links={};
    try{links.category_url=slug1}catch(e){};
    try{links.category_url=collections[langpack+"_lookup"][product.productType]}catch(e){};
    // console.log(links.category_url)
    links.category=lib[langpack].pharmacy;
    try{links.category=collections[langpack][slug1].title}catch(e){};
    try{links.category=collections[langpack][collections[langpack+"_lookup"][product.productType]].title}catch(e){};

    // links.collection_url=req.params.category;
    // links.collection=collections.en[collections_group].categories[req.params.category];
    links.product_url=slug2;

    if(amp=="amp"){
    //Build extra links for different languages for AMP
    links.trans_lang=slug2
    }else{
    //Build extra links for different languages
    links.trans_lang=collections["bm_translate"][slug1]+"/"+slug2;
    if(langpack!="en"){
        links.trans_lang=collections[langpack+"_translate"][slug1]+"/"+slug2;
    }

    }

    //Handle variants if in url else default
    let variant=0;
    if(req.query.vid){
    variant=returnVariantOrder(product.variants, req.query.vid);
    }

    //Get metafields product id
    let productId="";

    try{
    productId=getShopifyId(product.id);
    product.decodeId = productId
    }catch(e){
    console.log('Error cannot get product id',e.message)
    }

    //ADDED BY AMEERA: ONLY RUN THE FUNCTIONS FOR VARIANT URLS FOR 20 PRODUCTS ONLY (from product tag: seo1)
    let productFromAdmin = await getProductByAdminAPI(productId)
    //Initialization for variants
    let variant_url_data={}
    let variant_id={}
    //get tags
    let experiment_url = false;
    let product_tags=productFromAdmin.tags.split(", ")
    for(var i = 0; i < product_tags.length; i++){
    if(product_tags[i].indexOf('seo1') >= 0){
        experiment_url = true;
    }
    }

    //Only run variant if seo1 tag exist
    if(experiment_url == true){
    //Generate variant url, save to firebase
    variant_url_data = await generateVariantURL(product)
    //Add variant url to existing product data
    product = await updateVariantUrl(product, variant_url_data)

    //3.redirect ori handle to first variant
    if(variant_url_data && slug2===variant_url_data.product_handle){
        res.redirect(301, variant_url_data.query[0])
        return;
    }

    //Handle variant page
    //1. return variant id
    //2. return variant order
    //3. change title to variant title if its variant page
    if(slug2!=target){
        //1. return variant id
        variant_id = returnVariantData(product.variants, slug2)
        //Pass decoded id if there is variant id
        if(Object.keys(variant_id)[0]){
        product.decodeVid = getShopifyId(Object.keys(variant_id)[0])
        }
        //2. return variant order
        variant=returnVariantOrder(product.variants, Object.values(variant_id)[0]);
        //3. change title to variant title if its variant page
        if(variant_url_data.variant[Object.keys(variant_id)]){
        // product.title = product.title + " "+ variant_url_data.variant[Object.keys(variant_id)].v_title
        //get variant from the product details for accurate variant title
        product.title = product.title + " " + product.variants[variant].title

        }
    }
    }

    //
    //thisloop is going 3 times??? TODO: Figure out why??

    //Get metafield active ingredients
    var activeComplementProd = [];
    var saltArray = [];
    var arrayComplementProd = [];
    var tags;
    var product_salt = [];
    var questionTag=false;
    var hs_template;
    // array of the product type
    var product_type = ['prescriptiononlymeds', 'nonprescriptionmeds', 'otcdrugs', 'healthscreenings', 'covid', 'supplements', "healthcaredevices", "healthfooddrinks", "personalcare", "notforsale"];
    //Check if the product should have active ingredients
    if(product){
    //if(product.productType=="prescriptiononlymeds"||product.productType=="nonprescriptionmeds"||product.productType=="otcdrugs"){
    if(product_type.indexOf(product.productType)>=0){
    try{
        //Only fire if algolia fails
    if(arrayComplementProd.length==0){
        // console.log("Getting from shopify")
        //Look into shopify Admin API
        activeComplementProd = productFromAdmin;

        //console.log(activeComplementProd.tags)
        tags=activeComplementProd.tags.split(", ")

        for(var i = 0; i < tags.length; i++){
            // get all the salts in the fetched algolia product tag
            // console.log(tags[i].substring(0, 5))
        if(tags[i].substring(0, 5) == 'salt:'){
                saltArray.push(tags[i].substring(5,tags[i].length));
        }
        //get all therapy tags to find complement product
        if(tags[i].substring(0, 8) == 'therapy:'){
            arrayComplementProd.push("complement:"+tags[i].substring(8,tags[i].length));
        }
        //Get all question tags, take only one tag;
        // console.log(tags[i])
        if(questionTagLookup.indexOf(tags[i].replace("therapy:",""))>=0){
            // console.log("matched")
            questionTag=tags[i].replace("therapy:","");
        }

        //get health screening tags for different template
        if(tags[i].substring(0, 9) == 'template:'){
            hs_template=tags[i].substring(9, tags[i].length);
        }

        }

        //Check if its doc@home packages and amp pages, redirect to non amp pages
        if((hs_template == 'hs-home' && amp == 'amp') || (product.productType == 'healthscreenings'  && amp == 'amp')){
        let nonAmpUrl = config.subdir + "/" + langpack + "/health-screening/" + slug2
        if(langpack=='bm'){
            nonAmpUrl = config.subdir + "/saringan-kesihatan/" + slug2
        }
        return res.redirect(301, nonAmpUrl)
        }

    }
    }catch(e){
    //  console.log("Error at shopify admin product")
    console.log("Cannot get from Shopify Admin: "+e.message)
    }
    try{
    //  console.log("Starting salt arr")
    //   console.log(saltArray)
    var salt_faq = []
    if(saltArray.length > 0){
        for(var i = 0; i < saltArray.length; i++){
        //get salt data
        try{
            var splitSalt=saltArray[i].split("/") //Cater for salts with / between
            for(var j=0;j<splitSalt.length;j++){
            //Changed by Ameera on 18th March 2021: to remove '+' and '-' for space
            splitSalt[j] = splitSalt[j].replace("-"," ").replace(/[^\w\s]/gi,'').toLowerCase().trim().split(" ").join("-") // add - to salt with space
            product_salt.push(salts[splitSalt[j]])
            //get salts faq in product page if exist
            if(salts[splitSalt[j]]){
                if(salts[splitSalt[j]].faq){
                for(var k=0;k<salts[splitSalt[j]].faq.length;k++){
                    salt_faq.push(salts[splitSalt[j]].faq[k]) //push all faqs from all salts into new Array
                }
                }
            }
            }

        }
        catch(e){
            console.log("Error in getting salt data", e.message);
        }
        }
        try{
        //remove duplicate in salt faq and salt ref
        function getUniqueListBy(list, key) {
            return [...new Map(list.map(item => [item[key], item])).values()]
        }
        var newSalt_faq = getUniqueListBy(salt_faq, 'faq-qs')
        // console.log(newSalt_faq)
        salt_faq = newSalt_faq

        }catch(e){
        console.log("Error in remove duplicate salt faq",e.message)
        }
    }
    // console.log("XXXXXXXXXXXXXXXXXXXXXXXXXXxxPRODUCT Salt")
    //console.log(saltArray)

    }catch(e){
        console.log("Caught:",e.message)
    }
    }else{
    // console.log("Not medicine, skipping active ingredient")
    }
    }

    /*
        if there is an algolia product & a list of ATC
        1)Query algolia for related products & return complements
        2)Render page with complement variables
        */

        // Promise query, add to promise if exist
        var promiseQuery=[];

        // Frequently Bought Together/ therapy:
        //Prepare complement
        try{
        if(arrayComplementProd.length>0){            
            promiseQuery.push(getShopifyProduct(arrayComplementProd[0]))
        }else{
        //if there is no complement return empty promise
            promiseQuery.push(placeholderPromise())
        }
        } catch(e) {
        promiseQuery.push(placeholderPromise())
        }


        // similar products
        //Prepare substitutes promise
        //1. one salt and has symbol ' OR more than one salts, call algolia
        //2. if one salt only call graphql

        //!!!!Remove algolia and use shopify graphql
        // if((saltArray.length === 1 && saltArray[0].includes("'") > 0) || saltArray.length > 1 ) {
        //   promiseQuery.push(getAlgoliaProduct(saltArray.join(" ").replace(/[\/+%]/g, "-")))
        // }else
        if(saltArray.length>0){ 
        promiseQuery.push(getShopifyProduct("salt:" + saltArray.join(",").replace(/[\/+%]/g, "-")))
        }else{ // no salt
        promiseQuery.push(placeholderPromise())
        }
                

        //Prepare metaFields
        promiseQuery.push(returnMetafields(productId))

        //Prepare questions
        if(questionTag){
        // console.log("Getting question")
        // console.log(questionTag)
        promiseQuery.push(getQuestionByTag(questionTag))
        }else{
        promiseQuery.push(placeholderPromise())
        }

        // console.log("promiseQuery:")
        // console.log(promiseQuery)
        // console.log("starting promise run")
        Promise.all(promiseQuery).then(results=>{
        // console.log("XXXXXXXXXXXXXXXXXXXXXXXXXXxxCOMPLEMENTS")
        // console.log(results[0])
        // console.log(product.handle)
        // console.log("XXXXXXXXXXXXXXXXXXXXXXXXXXxxSUBSTITUES")
        // console.log(results[1].length)
        // console.log("XXXXXXXXXXXXXXXXXXXXXXXXXXxxMETAFIELDS")
        // console.log(results[2])
        // console.log("XXXXXXXXXXXXXXXXXXXXXXXXXXxxQuestions")
        // console.log(results[3].length)

        //Cleaned up results to remove duplicated variants
        // console.log("results[0]")
        // console.log(results[0])

        //Cleanup complements
        let complements=cleanUpShopifyComplements(results[0],product.handle);
        //to filter out complements that are out of stock
        try{
            if (complements) {
            complements = Object.values(complements).filter(data => data.inventory_quantity>0);
            }              
        }catch(e){
            console.log('error',e)
        }

        //cleanup substitutes
        let substitutes = []
        try{
            //if more than one salt  OR one salt but has symbol ' use algolia cleanup
            // if((saltArray.length === 1 && saltArray[0].includes("'") > 0) || saltArray.length > 1){ 
            //   substitutes=cleanUpAlgoliaSubstitutes(saltArray,results[1], product.handle);
            // }else if(saltArray.length === 1  ) {  // if one salt use graphql cleanup
            substitutes=cleanUpShopifySubstitutes(saltArray,results[1],product.handle);
            // }
        }
        catch(e){
            console.log("Error in cleaning up products for similar products", e.message)
        }
        

        //to filter out substitutes that are out of stock
        try{
            if(substitutes.length>0){
            substitutes = substitutes.filter(data => data.inventory_quantity>0);
            }
        }catch(e){
            console.log('error',e)
        }
        //substitutes = substitutes.filter(data => data.inventory_quantity>0);

        //console.log(substitutes)
        let metaFields=results[2];
        let questions=results[3];

        //Clean up metafields
        if(saltArray.length > 0){
            if(metaFields.schemaorg){
            metaFields.schemaorg.activeingredients = saltArray;
            } else {
            metaFields.schemaorg = {};
            metaFields.schemaorg.activeingredients = saltArray;
            }
        }

        //Decide which template to use
        var template_type = "product"
        //if type is health screening
        // if(tags){
        //   if(tags.indexOf('home-hs')>=0){ // for home health screening packages
        //     template_type = "screening"
        //   }
        //   if(tags.indexOf('hosp-hs')>=0){ // for hospital health screening packages
        //     template_type = "hospital_screening"
        //   }
        // }

        //Set Page Template
        var template='./playground/'+template_type+'.ejs'
        var amp_login=0;
        if(amp){
            template="./amphtml/amp_"+template_type+".ejs"
            template="./playground/amp/amp_"+template_type+"_v2.ejs"
        }
        let schemaorg = {}
        if(hs_template){

            // console.log("@@@@@@@@@@@@@@@@@@@@@@@@",hs_template)
            schemaorg = getSchemaData(metaFields, product);
            template = './screening_template/'+hs_template+'.ejs'
            if(amp){
            template = './amphtml/amp_screening_template/amp_'+hs_template+'.ejs'
            }
        }


        // console.log(req.cookies)
        if(req.cookies.doc_loggedin){
            amp_login=req.cookies.doc_loggedin;
        }

        if(links.category_url){
            req.apicacheGroup = links.category_url
        }
        //Render page

        // console.log("PRODUCT", product)

        //Check for specific url

        if(legacy.manual_translation[slug2] || legacy.manual_translation[slug1]){

            /*
            Check for BM language
                -Ensure pointing to correct translation link
                -Ensure pointing to right add to cart link
                -Ensure pointing to right metadata(canonical etc)
            */

            // Get the translated version of category. Example: supplements -> supplemen
            let translatedCategory = collections["bm_translate"][slug1]+"/";

            if(langpack!="en"){
            translatedCategory=collections[langpack+"_translate"][slug1]+"/";

            // Check if slug is English
            // 301 redirect to new bm slug
            if(!legacy.url[slug2]){
                return res.redirect(301,legacy.translation_link_pairs[slug2])
            }
            }
            // For AMP remove category and
            if(amp=="amp"){
            translatedCategory = ""
            }

            // Generate the trans_link to look up the translations.
            //For header lang button
            let translationLink = legacy.translation_link_pairs[slug2];

            if(!translationLink){
            translationLink = legacy.translation_link_pairs[slug1];
            };

            translationLink = translatedCategory + translationLink



            // Ensure product add to cart is also pointing to the correct version
            if(langpack !== "en"){

            // If it's BM language, change the product title. Capitalize the title as well.

            let capitalized = slug2.replace(/\-/g, " ").split(" ");

            for(var i = 0; i < capitalized.length; i++){
                capitalized[i] = capitalized[i].charAt(0).toUpperCase() + capitalized[i].slice(1)
            }

            product.title = capitalized.join(" ");

            // Handle redirect for BM pages for when the product is added to
            product.handle = slug2

            }

            // Assign translation link

            links.trans_lang = translationLink

        };

        //console.log(schemaorg)
        res.render(template, {
            amp_login:amp_login,
            collections: collections[langpack],
            curr_lang:langpack,
            templates : lib.templates[langpack],
            lang: lib[langpack],
            language: langpack,
            links:links,
            metaFields: metaFields,
            products: product,
            product_tags: tags,
            salts: salts_names,
            salt_data: product_salt, // all information in salt
            salt_faq: newSalt_faq, //salt faq
            url: lib.url,
            variant:variant,
            complements:complements, // returns complements array of objects
            substitutes:substitutes,
            questions:questions,
            mobileapp: mobileapp,
            productsAdmin: activeComplementProd,
            schemaorg : schemaorg,
            variant_url_data: variant_url_data,
            variant_id: variant_id,
            sanitizeHtml: sanitizeHtml
        });

        }).catch(d=>{
        console.log("Error at promise -> ", d)
        // console.log(d)
            return render404(req, res, langpack);
        })

});


function convertData(shopifyProducts) {
        if (!shopifyProducts) {
        // console.log("no shopifyProducts:")
        // console.log(shopifyProducts)
            return []
        }

        const variantsArray = [];
    
        shopifyProducts.forEach((product) => {
        const {
            id,
            title,
            handle,
            updated_at: updatedAt,
            tags,
            vendor,
            template_suffix: templateSuffix,
            product_type: productType,
            variants,
            images,
        } = product.node;

    function extractNumericPortion(id) {
        // Split the ID using '/'
        const parts = id.split('/');

        // Get the last part of the split ID
        const lastPart = parts[parts.length - 1];

        // Extract the numeric portion using regular expressions
        const numericPortion = lastPart.match(/\d+/);

        // Check if a numeric portion was found
        if (numericPortion) {
        return numericPortion[0];
        }

        // Return null if no numeric portion was found
        return null;
    }
    // function algolia -> shopify format
    variants.edges.forEach((variant) => {
        const {
            id: variantId,
            title: variantTitle,
            price,
            compare_at_price: compareAtPrice,
            sku,
            inventory_quantity: inventoryQuantity,
            position,
            product_image: image,
        } = variant.node;
        
        const variantData = {
            id: extractNumericPortion(id),
            objectID: extractNumericPortion(variantId),
            title,
            handle,
            updated_at: updatedAt,
            variant_title: variantTitle,
            price: parseFloat(price),
            compare_at_price: compareAtPrice,
            sku,
            inventory_quantity: inventoryQuantity,
            position,
            product_image: images.edges.map((edge) => edge.node.url),
            vendor,
            product_type: productType,
            tags,
        };

        variantsArray.push(variantData);
    });
    });

    return variantsArray;
}


// Dun Yan: Function to remove duplicates by price and ensuring the validity of the variants of the complements
function cleanUpShopifyComplements(resultsProd, handle){
// console.log("resultsProd:")
// console.log(resultsProd)
resultsProd = convertData(resultsProd);
var shopifyObj = {};
if(resultsProd.length>0){
    // To sort complements product from lower to higher prices
    resultsProd.sort(function(a,b){
    return (a.price - b.price);
    })

for(var i = 0 ; i < resultsProd.length;i++){
    //Check if valid item to be published
    //check if item is same as current product or not
    if(parseFloat(resultsProd[i].price)>0&&resultsProd[i].sku && resultsProd[i].handle !== handle){
    //console.log(resultsProd[i].id+ ': '+ resultsProd[i].price);
    // Check if product id exist & if current loop product price is less, take the higher price
    if(shopifyObj[resultsProd[i].id] && resultsProd[i].price >= shopifyObj[resultsProd[i].id].price){
        continue;
    }else{
        shopifyObj[resultsProd[i].id] = resultsProd[i];
    }

    }
}
return shopifyObj;
}else {
return shopifyObj
}
}






// API.JS
//2. Products API
//2.1. API to fetch all products
router.get('/products', function(req, res){
    request.get(shopifyURI + '/products', function(err, response, body){
        res.json(response.body);
    });
  });
  
//2.2. API to fetch single product based on handle
router.get('/products/:url', function(req, res, next){
    let handle = req.params.url;
    request.get(shopifyURI + '/products/' + handle, function(err, response, body){
    try{
        res.setHeader('Content-type','application/json')
        //Fixes for sdk response
        //Map back the price and compare at price from variant under price and compare at price obj
        let data = JSON.parse(response.body)
        //Get variants
        let variant =  data['variants']
        //Loop variants to get each variant price
        //Price need to parseFloat and get 2 d.p cause sdk returns price in string and 1 d.p
        for(var i=0; i<variant.length;i++){
        variant[i].price = parseFloat(variant[i].price.amount).toFixed(2)
        //For variant that doesn't have discount
        if(variant[i].compareAtPrice != null){
            variant[i].compareAtPrice = parseFloat(variant[i].compareAtPrice.amount).toFixed(2)
        }
        }
        res.send(data)
    }catch(e){
        res.send(body)
    }
    });
});

//2.2a. API to fetch single product by handle using admin API
router.get('/products/admin/:id', cache("5 minutes"), function(req, res, next){
    let handle = req.params.id;
    if(!handle){
    return res.status(400).send("Please provide a valid product Id")
    }
    request.get(shopifyURI + '/products/admin/'+handle, function(err, response, body){
    try{res.send(response.body);}catch(e){res.send(body)}
    });
});