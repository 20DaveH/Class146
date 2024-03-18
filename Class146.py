<!DOCTYPE html>
<html>

<head>
    <script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script>
</head>

<body>
    <a-scene background="color: #000000">

        <!--Camera-->
        <a-entity position="0 0 15">
            <a-camera></a-camera>
        </a-entity>


        <!--Sun-->
        <a-entity>
            <a-sphere position="0 0 0" radius="2" color="orange"></a-sphere>
        </a-entity>

        <!--Mercury-->
        <a-entity position="0 0 0" rotation="0 0 0"
            animation="property: rotation; to: 0 360 0;easing:linear; loop: true; dur: 20000">
            <a-sphere position="1  0 -5" radius="0.2" color="grey"></a-sphere>  
        </a-entity>

        <!--Venus-->
        <a-entity position="0 0 0" rotation="0 0 0"
            animation="property: rotation; to: 0 360 0;easing:linear; loop: true; dur: 25000">
            <a-sphere position="3  0 -5" radius="0.3" color="red"></a-sphere>  
        </a-entity>

        <!--Earth-->
        <a-entity position="0 0 0" rotation="0 0 0"
            animation="property: rotation; to: 0 360 0;easing:linear; loop: true; dur: 30000">
            <a-sphere position="5  0 -5" radius="0.4" color="blue"></a-sphere>  
        </a-entity>

        <!--Mars-->
        <a-entity position="0 0 0" rotation="0 0 0"
            animation="property: rotation; to: 0 360 0;easing:linear; loop: true; dur: 35000">
            <a-sphere position="7  0 -5" radius="0.4" color="brown"></a-sphere>  
        </a-entity>

        <!--Jupiter-->
        <a-entity position="0 0 0" rotation="0 0 0"
            animation="property: rotation; to: 0 360 0;easing:linear; loop: true; dur: 40000">
            <a-sphere position="9  0 -5" radius="1.2" color="orange"></a-sphere>  
        </a-entity>

        <!--Saturn-->
        <a-entity position="0 0 0" rotation="0 0 0"
            animation="property: rotation; to: 0 360 0;easing:linear; loop: true; dur: 45000">
            <a-sphere position= "11  0 -5" radius="0.9" color="red"></a-sphere>  
        </a-entity>

        <!--Uranus-->
        <a-entity position="0 0 0" rotation="0 0 0"
            animation="property: rotation; to: 0 360 0;easing:linear; loop: true; dur: 50000">
            <a-sphere position="13  0 -5" radius="0.6" color="blue"></a-sphere>  
        </a-entity>

        <!--Neptune-->
        <a-entity position="0 0 0" rotation="0 0 0"
            animation="property: rotation; to: 0 360 0;easing:linear; loop: true; dur: 55000">
            <a-sphere position="15  0 -5" radius="0.2" color="grey"></a-sphere>  
        </a-entity>
        
    </a-scene>
</body>

</html>


