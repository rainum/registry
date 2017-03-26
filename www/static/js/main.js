(function($) {
  var doctorId;

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
  var thisDay = moment().format('YYYY-MM-DD');

  moment.locale('ru');

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
        var date = target.date.format('YYYY-MM-DD');

        if (moment(date).isSameOrAfter(thisDay)) {
          console.log(date);

          getFreeSlots(date, doctorId);
        }
      }
    },
    constraints: {
      startDate: thisDay // Limit calendar by current day
    }
  });

  function showStep(index) {
    $('.step').hide(0);
    $('.step-' + index).show(0);
  }

  function getFreeSlots(date, id) {
    $('.time-container .loading').fadeIn(300);

    $.ajax({
      method: 'POST',
      url: '/static/free-slots.json',
      dataType: 'json',
      data: {
        doctorId: id,
        date: date
      }
    }).done(function(data) {
      var slotsHtml = data.map(function(slot) {
        if (slot.available) {
          return '<tr><td>' + slot.time + '</td><td><button class="btn btn-small btn-primary btn-pick-time">Обрати</button></td></tr>';
        }

        return '<tr class="active"><td>' + slot.time + '</td><td></td></tr>';
      });

      $('.time-container .table tbody').html(slotsHtml);

      $('.time-container .loading').fadeOut(300);
    });
  }

  $('.time-container').on('click', '.btn-pick-time', function(e) {
    e.preventDefault();
    $('.time-container .table tr').removeClass('success');

    var row = $(this).closest('tr');
    var time = row.find('td:first').text();

    row.addClass('success');

    console.log(time);
  });

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

    $(this).find('.loading').fadeIn(300);

    $.ajax({
      method: 'POST',
      url: '/select-address',
      dataType: 'json',
      data: dataObj
    }).done(function(data) {
      var doctor = data.doctor;

      doctorId = doctor.id;

      $('.doctor-name').text([
        doctor.last_name,
        doctor.first_name,
        doctor.second_name
      ].join(' '));

      getFreeSlots(thisDay, doctorId);
      showStep(2);
    }).always(function() {
      $('.loading').fadeOut(300);
    });

    return false;
  });
}($));