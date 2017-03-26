(function($) {
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  var csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });

  $('#street').chosen({
    disable_search_threshold: 10,
    placeholder_text_single: 'Оберіть вулицю'
  });

  $("#phone").mask("+380 (099) 999-99-99");

  var thisMonth = moment().format('YYYY-MM');

  $('.calendar').clndr({
    events: [
      /*{
        title: 'Multi-Day Event',
        endDate: thisMonth + '-14',
        startDate: thisMonth + '-10'
      }, {
        endDate: thisMonth + '-23',
        startDate: thisMonth + '-21',
        title: 'Another Multi-Day Event'
      }, {
        date: thisMonth + '-27',
        title: 'Single Day Event'
      }*/
    ],
    clickEvents: {
      click: function(target) {
        console.log('Cal-1 clicked: ', target.date.format('YYYY-MM-DD'));
      }
    },
    multiDayEvents: {
      singleDay: 'date',
      endDate: 'endDate',
      startDate: 'startDate'
    },
    showAdjacentMonths: true,
    adjacentDaysChangeMonth: false,
    constraints: {
      startDate: moment().format('YYYY-MM-DD') // Limit calendar by current day
    }
  });

  function showStep(index) {
    $('.step').hide(0);
    $('.step-' + index).show(0);
  }

  $('.prev-step').on('click', function(e) {
    e.preventDefault();
    showStep(1);
  });

  $('.step.step-1 form').on('submit', function(e) {
    e.preventDefault();

    var dataArr = $(this).serializeArray();
    var dataObj = dataArr.reduce(function(acc, field) {
      acc[field.name] = field.value;
      return acc;
    }, {});

    $('.loading').fadeIn(300);

    $.ajax({
      method: 'POST',
      url: '/select-address',
      dataType: 'json',
      data: dataObj
    }).done(function() {
      console.log("success");
    }).always(function() {
      $('.loading').fadeOut(300);
      showStep(2);
    });

    return false;
  });
}($));