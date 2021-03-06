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

        this.search_results_container = $("#search-results-tab #search-results-container");
        this.last_search_query_string = null;

        this.search_loaded_articles_count = () => {
            return $("#search-results-container article").length;
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
                this.all_articles_container.append(response);
            }
        });
    }

    search_articles(query_string) {
        $.ajax({
            type: "GET",
            url: "/search",
            data: {
                'query_string': query_string,
                'fetch_count': 10
            },
            dataType: "html",
            success: (response) => {
                this.last_search_query_string = query_string;

                this.activate_tab("search-results");
                this.search_results_container.html('');
                this.search_results_container.append(response);
            },
            statusCode: {
                404: (response) => {
                    $("#no-search-results-message").text(response.responseText);
                    $("#no-search-results-message").toggleClass("d-none show");

                    setTimeout(() => {
                        $("#no-search-results-message").toggleClass("d-none show");
                    }, 3000);
                }
            }
        });
    }

    search_more(fetch_count) {
        $.ajax({
            type: "GET",
            url: "/search/load_more",
            data: {
                'last_search_query_string': this.last_search_query_string,
                'search_loaded_articles_count': this.search_loaded_articles_count(),
                'fetch_count': fetch_count
            },
            dataType: "html",
            success: (response) => {
                this.search_results_container.append(response);
            }
        });
    }
}

window.content_browser = new ContentBrowser("#content-browser");
