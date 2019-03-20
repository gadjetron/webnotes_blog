class ContentBrowser {

    constructor(root_element_id) {
        this.root_element_id = root_element_id;
        this.root = $(root_element_id);

        this.tabs = {
            'all-articles': $(`${this.root_element_id} a[href="#all-articles-tab"]`),
            'opened-articles': $(`${this.root_element_id} a[href="#opened-articles-tab"]`),
            'search-results': $(`${this.root_element_id} a[href="#search-results-tab"]`)
        }

        this.active_tab = this.tabs["all-articles"];

        this.opened_article_container = $("#opened-articles-tab #opened-article-container");
    }

    activate_tab(tab_name) {
        if ((tab_name in this.tabs)) {
            this.tabs[tab_name].tab("show");
            this.active_tab = this.tabs[tab_name];
        }
        else {
            throw new Error("Such tab doesn't exist!");
        }
    }

    load_article(url) {
        $.ajax({
            type: "GET",
            url: url,
            dataType: "html",
            success: (response) => {
                this.activate_tab("opened-articles");
                this.opened_article_container.html(response);
            }
        });
    }
}

window.content_browser = new ContentBrowser("#content-browser");
