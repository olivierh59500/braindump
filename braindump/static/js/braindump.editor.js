(function(window) {
    'use strict';

    /**
     * Braindump editor module
     *
     * Creates keyboard shortcuts that are activated inside
     * of the editor textarea.
     */

    var editor = document.getElementById('editor');

    editor.addEventListener('keydown', function(e) {
        // Enable Tabbing inside of Text Area
        // From http://stackoverflow.com/a/18303822
        if (e.keyCode === 9) {
            var start = this.selectionStart;
            var end = this.selectionEnd;

            var target = e.target;
            var value = target.value;

            // Insert 4 spaces instead of a tab character
            target.value = value.substring(0, start)
                + "    "
                + value.substring(end);

            this.selectionStart = this.selectionEnd = start + 4;

            e.preventDefault();
        }
        // Insert current date at cursor position
        if(e.altKey && e.keyCode == 'D'.charCodeAt(0)){
            e.preventDefault();
            console.log("Doing stuff");
        }
    });

})(window);