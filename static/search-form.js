const config = {
  placeHolder: "病気を検索",
  data: {
    src: async (query) => {
      try {
        // Fetch Data from external Source
        const source = await fetch(`/api/search?word=${query}`);
        // Data should be an array of `Objects` or `Strings`
        const data = await source.json();

        return data.map((item) => item.word);
      } catch (error) {
        return error;
      }
    },
    //　cache: true,
  },
  resultItem: {
    highlight: true,
  },
  events: {
    input: {
      selection: (event) => {
        const selection = event.detail.selection.value;
        autoCompleteJS.input.value = selection;
        location.href = `/words/${event.detail.selection.value}`;
      },
    },
  },
  submit: true,
};

const autoCompleteJS = new autoComplete(config);

document
  .getElementById("search-form")
  .addEventListener("submit", (e) => {
    e.preventDefault();

    const input = document.querySelector("#search-form input");
    location.href = `/words/${input.value}`;
  });
