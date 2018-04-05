/*var loadingBlock = "<div class='sk-folding-cube'>" +
    "<div class='sk-cube1 sk-cube'></div>" +
    "<div class='sk-cube2 sk-cube'></div>" +
    "<div class='sk-cube4 sk-cube'></div>" +
    "<div class='sk-cube3 sk-cube'></div>" + "</div>";*/
var loadingBlock = "<div class='spinner'></div>";
var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

console.log("CSRF : " + csrftoken);
$(function () {
    updateStatus();
    setInterval(updateStatus, 3000);
});

function updateStatus() {
    $.post("http://localhost:8000/seocheck/ajax/",
        {},
        function (data, status) {
            console.log(data);
            $('#dataDisplay').html(JSON.stringify(data));
            fill_all(data);
        });
}

function fill_all(data) {
    fill_task_1_get_css_status("#task_css", data);
    fill_task_2_get_keyword_density("#keyword_density", data)
    fill_task_3_get_sitemap_list("#sitemap", data)
}

function fill_task_1_get_css_status(row, data) {
    $(row + " .left-cell").html("Inline CSS Test");
    if (!data['result']['task_1_get_css_status']) {
        if ($(row).data('final') === "true") return;
        $(row + " .right-cell").html(loadingBlock);
        $(row).data('final', 'true')
    }
    else {
        $(row + " .right-cell").html(data['result']['task_1_get_css_status']['bad'])
    }
}

function fill_task_2_get_keyword_density(row, data) {
    $(row + " .left-cell").html("Most Common Keywords Test");
    if (!data['result']['task_2_get_keyword_density']) {
        if ($(row).data('final') === "true") return;
        $(row + " .right-cell").html(loadingBlock);
        $(row).data('final', 'true')
    } else {
        var renderedList = "";
        wordList = data['result']['task_2_get_keyword_density'];
        for (var i = 0; i < wordList.length; i++) {
            renderedList += "<li>" + wordList[i][0] + " - " + wordList[i][1] + "</li>"
        }
        $(row + " .right-cell").html("<ol>" + renderedList + "</ol>");
    }

}

function fill_task_3_get_sitemap_list(row, data) {
    $(row + " .left-cell").html("Sitemap Test");
    var result = data['result']['task_3_get_sitemap_list'];
    if (!result) {
        setSpinner(row);
    } else {
        render_task_3_get_sitemap_list(row, result)
    }
}

//====================== RENDERING ================================
function render_task_3_get_sitemap_list(row, result) {
    clearRow(row);
    status = getStatus(result);
    data = getData(result);
    msg = getMessage(result);
    var renderedList = "";
    for (var i = 0; i < data.length; i++) {
        renderedList += "<li><a href='" + data[i] + "'>" + data[i] + "</a></li>"
    }
    appendToRow(row, msg + "<br>");
    appendToRow(row, "<ol>" + renderedList + "</ol>");
    setStatusIcon(row, status)
}

//_________________________________________________________

function setSpinner(row) {
    if ($(row).data('is-spinner') === "true") return;
    $(row + " .right-cell").html(loadingBlock);
    $(row).data('is-spinner', 'true');
}


function setStatusIcon(row, status) {
    var statusIcon = ['fa-hourglass-half', 'fa-check', 'fa-times', 'fa-exclamation'];
    var iconElem = $(row + " .stat-cell i");
    if (status === 'waiting') {
        iconElem.attr('class', 'fas ' + statusIcon[0])
    }
    if (status === 'ok') {
        iconElem.attr('class', 'fas ' + statusIcon[1])
    }
    if (status === 'error') {
        iconElem.attr('class', 'fas ' + statusIcon[2])
    }
    if (status === 'warning') {
        iconElem.attr('class', 'fas ' + statusIcon[3])
    }

}

function getStatus(result) {
    return result['status']
}

function getData(result) {
    return result['data']
}

function getMessage(result) {
    return result['message']
}

function clearRow(row) {
    $(row + " .right-cell").html('');
}

function appendToRow(row, str) {
    $(row + " .right-cell").append(str);
}

function prependToRow(row, str) {
    $(row + " .right-cell").prepend(str);
}

