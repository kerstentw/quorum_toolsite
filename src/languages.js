const LANGUAGES = require("lang_keys").LANGUAGES;

module.exports.languageSwitcher = (_tag) => {
    let cur_language = LANGUAGES[_tag] || LANGUAGES["Ko"]
    return cur_language;
}
