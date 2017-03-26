(function($) {
  var data = {
    step1: {},
    step2: {}
  };

  $('#street').chosen({
    disable_search_threshold: 10,
    placeholder_text_single: 'Оберіть вулицю'
  });

  $("#phone").mask("+380 (099) 999-99-99");

  var thisMonth = moment().format('YYYY-MM');

  $('.calendar').clndr({
    events: [
      {
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
      }
    ],
    clickEvents: {
      click: function(target) {
        console.log('Cal-1 clicked: ', target);
      },
      today: function() {
        console.log('Cal-1 today');
      },
      nextMonth: function() {
        console.log('Cal-1 next month');
      },
      previousMonth: function() {
        console.log('Cal-1 previous month');
      },
      onMonthChange: function() {
        console.log('Cal-1 month changed');
      },
      nextYear: function() {
        console.log('Cal-1 next year');
      },
      previousYear: function() {
        console.log('Cal-1 previous year');
      },
      onYearChange: function() {
        console.log('Cal-1 year changed');
      },
      nextInterval: function() {
        console.log('Cal-1 next interval');
      },
      previousInterval: function() {
        console.log('Cal-1 previous interval');
      },
      onIntervalChange: function() {
        console.log('Cal-1 interval changed');
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

  $('#step-1-form').on('submit', function(e) {
    e.preventDefault();

    var dataArr = $(this).serializeArray();
    var dataObj = dataArr.reduce(function(acc, field) {
      acc[field.name] = field.value;
      return acc;
    }, {});

    data.step1 = dataObj;

    showStep(2);
  });
}($));