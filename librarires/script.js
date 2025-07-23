const date = document.getElementById("date");


const btn = document.getElementById("btn");

btn.addEventListener(
    "click", () => {
        const dateStr = date.value;
        console.log(dateStr)

        if (dateStr === "2025-07-23"){
        const active = document.querySelectorAll(".👀")
        active.forEach(
            eyes => {
                eyes.classList.toggle("noActive")
            }
        )
        }
    }
)

