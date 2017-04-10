<?php
/**
 * Created by PhpStorm.
 * User: vvv
 * Date: 2017/3/24
 * Time: 22:15
 */
$page = $_GET['page'];
$date = $_GET['date'];
/*echo $page.$date;*/
$conn = new mysqli('localhost','root','zht1741105','news');
if(mysqli_connect_errno()){
    echo "数据库连接失败";
}
mysqli_query($conn,'SET NAME utf-8');

$conn->query("SET NAMES utf8");
$str = "SELECT title,time,content FROM news WHERE page = '$page' AND newsdate = '$date';";
$rs = $conn->query($str);
$res = $rs->fetch_array();
if($res==""){
    echo "没有这天的新闻，请爬取后查询";
}else {


    while ($province = $rs->fetch_array()) {
        $title[] = $province['title'];
        $time[] = $province['time'];
        $content[] = $province['content'];
    }
    for ($i = 0; $i < sizeof($title); $i++) {
        echo '<p>' . $title[$i] . '<p/><br/><br/><p>' . $time[$i] . '</p><br/><br/>' . $content[$i] . '<br/><br/><br/><br/>';
    }
}

?>