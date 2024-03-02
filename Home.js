(function () {
    'use strict';

    Office.onReady(function() {
        // 当Office应用程序准备就绪时执行
        $(document).ready(function () {
            // DOM准备好后绑定事件
            $('#set-color').on("click", setColor);
        });
    });

    async function setColor() {
        try {
            await Excel.run(async (context) => {
                // 获取选中的范围
                const range = context.workbook.getSelectedRange();
                // 设置填充色为绿色
                range.format.fill.color = 'green';
                
                await context.sync(); // 同步更改到Excel应用
            });
        } catch (error) {
            console.error("Error: ", error);
            if (error instanceof OfficeExtension.Error) {
                console.log("Debug info: " + JSON.stringify(error.debugInfo));
            }
        }
    }
})();
