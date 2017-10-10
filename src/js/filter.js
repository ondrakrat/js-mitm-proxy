/**
 * Created by Ondřej Kratochvíl on 10.10.17.
 */
if (parent.document.URL !== document.location.href)
    throw new Error("Not the main page");

(function (e) {
    e.setAttribute("src", "alert.js");
    document.getElementsByTagName("body")[0].appendChild(e);
})
(document.createElement("script"));
void(0);