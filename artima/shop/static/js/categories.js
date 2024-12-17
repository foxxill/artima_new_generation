document.addEventListener('DOMContentLoaded', () => {
    const categoriesButton = document.getElementById('categoriesButton');
    const categoriesPanel = document.getElementById('categoriesPanel');

    categoriesButton.addEventListener('click', (event) => {
        event.stopPropagation();
        categoriesPanel.classList.toggle('dropdown-content');
    });

    document.addEventListener('click', (event) => {
        if (!categoriesPanel.contains(event.target) && event.target !== categoriesButton) {
            categoriesPanel.classList.add('dropdown-content');
        }
    });

    categoriesPanel.addEventListener('click', (event) => {
        event.stopPropagation();
    });
});
