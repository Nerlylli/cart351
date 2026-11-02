window.onload = function () {
    console.log("post js is loaded");
    document
        .querySelector("#insertPlantFormFetchPost")
        .addEventListener("submit", async function (event) {
            event.preventDefault();
            console.log("post form clicked")

            let form = document.querySelector("#insertPlantFormFetchPost");
            let data = new FormData(form);
            console.log(data);
            try {
                let res = await fetch("/postPlantFormFetch", {
                    method: "POST",
                    body: data,
                });
                let resJSON = await res.json();
                console.log(resJSON);
            } catch (err) {
                console.log(err);
            }


        })
};