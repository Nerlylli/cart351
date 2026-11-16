// DATA
window.onload = function () {
    console.log("loaded script_post_form.js");
    document
        .querySelector("#getUserInfo")
        .addEventListener("submit", async function (event) {
            event.preventDefault();
            console.log("button clicked");
            const htmlForm = document.querySelector("#getUserInfo");
            const formData = new FormData(htmlForm);

            const user = Object.fromEntries(formData.entries());

            try {
                let res = await fetch("/getData", {
                    method: "POST",
                    body: formData,
                });
                let resJSON = await res.json();
                console.log(resJSON);

                displayProfile(user);

            } catch (err) {
                console.log(err);
            }
        });
};