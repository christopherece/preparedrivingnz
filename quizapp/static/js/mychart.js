<script>
  $(document).ready(function() {
    $.ajax({
        url: "{% url 'feedback_count' %}",
        dataType: "json",
        success: function(data) {
            var labels = ['Excellent', 'Good', 'Average', 'Poor', 'Bad'];
            var counts = [0, 0, 0, 0, 0];

            for (var i = 0; i < data.length; i++) {
                if (data[i].rating === 'Excellent') {
                    counts[0] = data[i].total;
                } else if (data[i].rating === 'Good') {
                    counts[1] = data[i].total;
                } else if (data[i].rating === 'Average') {
                    counts[2] = data[i].total;
                } else if (data[i].rating === 'Poor') {
                    counts[3] = data[i].total;
                } else if (data[i].rating === 'Bad') {
                    counts[4] = data[i].total;
                }
            }

            var ctx = document.getElementById('myChart').getContext('2d');
            var chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Feedback Counts',
                        data: counts,
                        backgroundColor: [
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(153, 102, 255, 0.2)'
                        ],
                        borderColor: [
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(255, 99, 132, 1)',
                            'rgba(153, 102, 255, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                                precision: 0
                            }
                        }]
                    }
                }
            });

            // add onClick event listener to chart
            chart.canvas.onclick = function(evt) {
                var activeBars = chart.getElementsAtEvent(evt);

                if (activeBars.length > 0) {
                    var index = activeBars[0]._index;
                    var ratingLabel = chart.data.labels[index];

                    // get feedback based on rating
                    $.ajax({
                        url: "{% url 'feedback_count' %}",
                        data: {
                            'rating': ratingLabel
                        },
                        dataType: "json",
                        success: function(data) {
                            var feedback = data[0];

                            // redirect to corresponding feedback detail page
                            if (ratingLabel === 'Excellent') {
                                window.location.href = "{% url 'excellent_feedback' %}?" +
                                    "user=" + feedback.user + "&" +
                                    "comment=" + feedback.comment + "&" +
                                    "rating=" + feedback.rating + "&" +
                                    "date=" + feedback.feedback_date;
                            } else if (ratingLabel === 'Good') {
                                window.location.href = "{% url 'good_feedback' %}?" +
                                    "user=" + feedback.user + "&" +
                                    "comment=" + feedback.comment + "&" +
                                    "rating=" + feedback.rating + "&" +
                                    "date=" + feedback.feedback_date;
                            } else if (ratingLabel === 'Average') {
                                window.location.href = "{% url 'average_feedback' %}?" +
                                    "user=" + feedback.user + "&" +
                                    "comment=" + feedback.comment + "&" +
                                    "rating=" + feedback.rating + "&" +
                                    "date=" + feedback.feedback_date;
                            } else if (ratingLabel === 'Poor') {
                                window.location.href = "{% url 'poor_feedback' %}?" +
                                    "user=" + feedback.user + "&" +
                                    "comment=" + feedback.comment + "&" +
                                    "rating=" + feedback.rating + "&" +
                                    "date=" + feedback.feedback_date;
                            } else if (ratingLabel === 'Bad') {
                                window.location.href = "{% url 'bad_feedback' %}?" +
                                    "user=" + feedback.user + "&" +
                                    "comment=" + feedback.comment + "&" +
                                    "rating=" + feedback.rating + "&" +
                                    "date=" + feedback.feedback_date;
                            }
                        }
                    });
                }
            };

        }
    })
});   
</script>