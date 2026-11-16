// BIRTHDAY DATE - INTO AGE
function calculateAge(birthday) {
    const today = new Date();
    const birthDate = new Date(birthday + "T00:00:00");
    let age = today.getFullYear() - birthDate.getFullYear();
    const month = today.getMonth() - birthDate.getMonth();
    if (
        month < 0 ||
        (month === 0 && today.getDate() < birthDate.getDate())
    ) {
        age--;
    }
    return age;
}

// FORM TURNS INTO USER INFOBOX
function displayProfile(user) {
    const form = document.querySelector("#getUserInfo");
    const template = document.querySelector("#userProfile");
    const profile = template.cloneNode(true);
    profile.style.display = "block";

    // NAME
    const name = user.u_name

    // AGE
    const age = calculateAge(user.b_date);
    const birthday = new Date(user.b_date + "T00:00:00");
    const formattedBirthday = birthday.toLocaleDateString("en-US", {
        month: "long",
        day: "numeric",
        year: "numeric"
    });

    // WHO ARE YOU?
    profile.querySelector("#profileName").textContent = name;
    profile.querySelector("#profilePronouns").textContent =
        `Pronouns: ${user.Pronouns}`;
    profile.querySelector("#profileAge").textContent =
        `${name} is ${age} years old.`;
    profile.querySelector("#profileBirthday").textContent =
        `${name}'s birthday is ${formattedBirthday}.`;

    // WHAT ARE YOUR FAVORITES?
    profile.querySelector("#profileGeneral").textContent =
        `Favorite general interests are: ${user.t_general}`;
    profile.querySelector("#profileColor").textContent =
        `Favorite color is: ${user.f_color}`;
    profile.querySelector("#profileMusic").textContent =
        `Favorite music are: ${user.t_music}`;
    profile.querySelector("#profileMovies").textContent =
        `Favorite movies are: ${user.t_movies}`;
    profile.querySelector("#profileShows").textContent =
        `Favorite shows are: ${user.t_tv}`;
    profile.querySelector("#profileGames").textContent =
        `Favorite games are: ${user.t_games}`;
    profile.querySelector("#profileBooks").textContent =
        `Favorite books are: ${user.t_books}`;

    // DETAILS
    profile.querySelector("#profileHereFor").textContent =
        `I am here for: ${user.p_name}`;
    profile.querySelector("#profileStatus").textContent =
        `Relationship status: ${user["Relationship-Status"]}`;
    profile.querySelector("#profileSexuality").textContent =
        `Sexuality: ${user.Sexuality}`;
    profile.querySelector("#profileEthnicity").textContent =
        `Ethnicity: ${user.Ethnicity}`;
    profile.querySelector("#profileZodiac").textContent =
        `Zodiac sign: ${user.Zodiac}`;
    profile.querySelector("#profileOccupation").textContent =
        `Occupation: ${user.o_name}`;

    document.querySelector("#getUserInfo").replaceWith(profile);
}