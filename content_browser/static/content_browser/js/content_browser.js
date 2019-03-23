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
        this.all_articles_container = $("#all-articles-tab #all-articles-container");

        this.loaded_articles_count = () => {
            return $("#all-articles-container article").length;
        }
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

    load_more_articles(fetch_count) {
        $.ajax({
            url: '/articles/load_more',
            type: 'GET',
            dataType: 'html',
            data: {
                'loaded_articles_count': this.loaded_articles_count(),
                'fetch_count': fetch_count
            },
            success: (response) => {
                this.all_articles_container.prepend(response);
            }
        });
    }
}

window.content_browser = new ContentBrowser("#content-browser");
