document.addEventListener('DOMContentLoaded', () => {
    const categoriesButton = document.getElementById('categoriesButton');
    const categoriesPanel = document.getElementById('categoriesPanel');

    categoriesButton.addEventListener('click', (event) => {
        event.stopPropagation();
        categoriesPanel.classList.toggle('dropdown-content');
    });

    document.addEventListener('click', () => {
        if (!categoriesPanel.classList.contains('dropdown-content')) {
            categoriesPanel.classList.add('dropdown-content');
        }
    });

    categoriesPanel.addEventListener('click', (event) => {
        event.stopPropagation();
    });
});
