(function(window) {
    'use strict';

    /**
     * Braindump keyboard shortcuts module
     */

    var docsLocation = document.getElementById('shortcutDocs');
    var addNoteButton = document.getElementById('addNoteButton');

    onkeydown = function(e){
        if(e.altKey && e.keyCode == 'D'.charCodeAt(0)){
            e.preventDefault();
            console.log("Doing stuff");
        }
        if(e.keyCode == 'N'.charCodeAt(0)){
            e.preventDefault();
            addNoteButton.click()
        }
    }

    /**
     * Append docs about shortcuts to the main window once it has loaded.
     * This also partially serves as a canary to ensure that the JS is working
     * properly.
     */
    window.addEventListener('load', function() {
        var shortcutDocs = `
        <div id="shortcutDocs">
            <strong>Keyboard Shortcuts</strong>
            <ul class="shortcuts">
                <li>n : Add new Note</li>
                <li>b : Add new Notebook</li>
                <li>a : Go to Archive</li>
                <li>f : Go to Favorites</li>
                <li>t : Go to Trash</li>
                <li>Ctrl + d : Insert current Date (into textfield)</li>
            </ul>
        </div>
        `
        docsLocation.innerHTML += shortcutDocs;
    });

})(window);