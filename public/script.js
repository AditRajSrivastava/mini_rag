document.addEventListener('DOMContentLoaded', () => {

    // --- CONFIGURATION ---
    // TODO: Replace this with your DEPLOYED backend URL from Render.
    const API_BASE_URL = "https://mini-rag-y8lh.onrender.com"; // Use this for local testing

    // --- DOM ELEMENT REFERENCES ---
    const uploadBtn = document.getElementById('upload-btn');
    const queryBtn = document.getElementById('query-btn');
    const uploadStatus = document.getElementById('upload-status');
    const answerDiv = document.getElementById('answer');
    const sourcesDiv = document.getElementById('sources');
    const resultsContainer = document.getElementById('results-container');
    const contextText = document.getElementById('context-text');
    const queryInput = document.getElementById('query-input');
    
    // Loader elements
    const uploadLoader = document.getElementById('upload-loader');
    const queryLoader = document.getElementById('query-loader');
    
    // --- HELPER FUNCTIONS ---
    
    /**
     * Toggles the loading state for a button.
     * @param {HTMLButtonElement} button - The button element.
     * @param {boolean} isLoading - True to show loader, false to hide.
     */
    const toggleButtonLoading = (button, isLoading) => {
        if (isLoading) {
            button.classList.add('loading');
            button.disabled = true;
        } else {
            button.classList.remove('loading');
            button.disabled = false;
        }
    };

    // --- EVENT LISTENERS ---

    // Event Listener for the Upload Button
    uploadBtn.addEventListener('click', async () => {
        const text = contextText.value.trim();
        if (!text) {
            uploadStatus.textContent = 'Please paste some text to upload.';
            uploadStatus.style.color = '#ff6b6b';
            return;
        }
        
        toggleButtonLoading(uploadBtn, true);
        uploadStatus.textContent = 'Embedding document... this may take a moment.';
        uploadStatus.style.color = '#a0a0a0';
        resultsContainer.classList.add('hidden');

        try {
            const response = await fetch(`${API_BASE_URL}/upload`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: text })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
            }

            const result = await response.json();
            uploadStatus.textContent = result.message;
            uploadStatus.style.color = '#2ecc71'; // Green for success
        } catch (error) {
            console.error('Upload Error:', error);
            uploadStatus.textContent = `Upload failed: ${error.message}`;
            uploadStatus.style.color = '#ff6b6b'; // Red for error
        } finally {
            toggleButtonLoading(uploadBtn, false);
        }
    });

    // Event Listener for the Query Button
    queryBtn.addEventListener('click', async () => {
        const question = queryInput.value.trim();
        if (!question) {
            alert('Please enter a question.');
            return;
        }

        toggleButtonLoading(queryBtn, true);
        resultsContainer.classList.add('hidden'); // Hide old results
        answerDiv.textContent = '';
        sourcesDiv.innerHTML = '';

        try {
            const response = await fetch(`${API_BASE_URL}/query`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question: question })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
            }

            const result = await response.json();
            displayResults(result);

        } catch (error) {
            console.error('Query Error:', error);
            answerDiv.textContent = `Error getting answer: ${error.message}`;
            resultsContainer.classList.remove('hidden');
        } finally {
            toggleButtonLoading(queryBtn, false);
        }
    });
    
    /**
     * Displays the results in the UI.
     * @param {object} result - The result object from the API.
     */
    const displayResults = (result) => {
        // Sanitize and format the answer to handle citations like [1]
        let formattedAnswer = result.answer.replace(/</g, "&lt;").replace(/>/g, "&gt;");
        formattedAnswer = formattedAnswer.replace(/\[(\d+)\]/g, '<strong>[$1]</strong>');
        
        answerDiv.innerHTML = formattedAnswer;

        if (result.sources && result.sources.length > 0) {
            let sourcesHTML = '<ul>';
            result.sources.forEach(source => {
                const sanitizedContent = source.content.replace(/</g, "&lt;").replace(/>/g, "&gt;");
                sourcesHTML += `<li><strong>[${source.position}]</strong>: ${sanitizedContent}</li>`;
            });
            sourcesHTML += '</ul>';
            sourcesDiv.innerHTML = sourcesHTML;
        }

        resultsContainer.classList.remove('hidden');
    };

});