window.onload = function () {
    console.log("script loaded")
    document
        .querySelector("#insertPlantFormFetch")
        .addEventListener("submit",
            async function (event) {
                event.preventDefault();
                console.log("button clicked");
                const htmlForm = document.querySelector("#insertPlantFormFetch");
                const formula = new FormData(htmlForm);
                // console.log(htmlForm)
                const queryParams = new URLSearchParams(formData).toString();
                const url = `/getDataFromForm?${queryParams}`;

                try {
                    let res = await fetch(url)
                    let resJSON = await res.json()
                    console.log(resJSON)

                    document.querySelector("#result-container").innerHTML +=
                        ` THE NEW RESULT: ${resJSON.data_received}
                        OWNER NAME : ${resJSON.owner}
                        PLANT NAME : ${resJSON.plantname}`

                }
                catch (err) {
                    console.log(err)
                }
            });
};