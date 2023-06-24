const BUCKET_URL = "https://industry-darlings-improv.s3.amazonaws.com"

fetch(BUCKET_URL)
    .then(response => response.text())
    .then(data => {
        const parser = new DOMParser();
        xml = parser.parseFromString(data, "application/xml");
        ParseXML(xml)
    })
    .catch(console.error);

function ParseXML(xml) {
    tableNode = document.getElementById("files")

    var contents = [...xml.getElementsByTagName("Contents")];
    contents.forEach(item => {
        var itemKey = item.getElementsByTagName("Key")[0].innerHTML
        var itemSize = item.getElementsByTagName("Size")[0].innerHTML
        var itemSizeInMB = (10 * Math.round(itemSize / (1024 ** 2)) / 10)


        if (!(itemKey.endsWith("/") || itemKey == "error.html" || itemKey == "index.html" || itemKey == "script.js")) {
            var newRow = tableNode.insertRow(-1);
            fileLink = `${BUCKET_URL}/${itemKey}`

            newRow.innerHTML = `<td scope="row"><a href=${fileLink}>${itemKey}</a></td><td class='file-size text-end'>${itemSizeInMB}M</td>`
        }
    })
}